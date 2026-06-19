from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import os

from .models import (
    Reporter,
    Issue,
    CriticalIssue,
    LowPriorityIssue
)

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

REPORTERS_FILE = os.path.join(
    BASE_DIR,
    "reporters.json"
)

ISSUES_FILE = os.path.join(
    BASE_DIR,
    "issues.json"
)


@csrf_exempt
def reporters(request):

    if request.method == "GET":

        reporter_id = request.GET.get("id")

        with open(REPORTERS_FILE, "r") as f:
            reporters_data = json.load(f)

        # GET single reporter
        if reporter_id:

            reporter_id = int(reporter_id)

            for reporter in reporters_data:

                if reporter["id"] == reporter_id:
                    return JsonResponse(
                        reporter,
                        status=200
                    )

            return JsonResponse(
                {"error": "Reporter not found"},
                status=404
            )

        # GET all reporters
        return JsonResponse(
            reporters_data,
            safe=False,
            status=200
        )

    elif request.method == "POST":

        try:

            data = json.loads(request.body)

            reporter = Reporter(
                data["id"],
                data["name"],
                data["email"],
                data["team"]
            )

            reporter.validate()

            with open(REPORTERS_FILE, "r") as f:
                reporters_data = json.load(f)

            reporters_data.append(
                reporter.to_dict()
            )

            with open(REPORTERS_FILE, "w") as f:
                json.dump(
                    reporters_data,
                    f,
                    indent=4
                )

            return JsonResponse(
                reporter.to_dict(),
                status=201
            )

        except ValueError as e:

            return JsonResponse(
                {"error": str(e)},
                status=400
            )


@csrf_exempt
def issues(request):

    if request.method == "GET":

        issue_id = request.GET.get("id")
        status_filter = request.GET.get("status")

        with open(ISSUES_FILE, "r") as f:
            issues_data = json.load(f)

        # GET single issue
        if issue_id:

            issue_id = int(issue_id)

            for issue in issues_data:

                if issue["id"] == issue_id:
                    return JsonResponse(
                        issue,
                        status=200
                    )

            return JsonResponse(
                {"error": "Issue not found"},
                status=404
            )

        # GET issues by status
        if status_filter:

            filtered_issues = []

            for issue in issues_data:

                if issue["status"] == status_filter:
                    filtered_issues.append(issue)

            return JsonResponse(
                filtered_issues,
                safe=False,
                status=200
            )

        # GET all issues
        return JsonResponse(
            issues_data,
            safe=False,
            status=200
        )

    elif request.method == "POST":

        try:

            data = json.loads(request.body)

            if data["priority"] == "critical":

                issue = CriticalIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            elif data["priority"] == "low":

                issue = LowPriorityIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            else:

                issue = Issue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )

            issue.validate()

            with open(ISSUES_FILE, "r") as f:
                issues_data = json.load(f)

            issues_data.append(
                issue.to_dict()
            )

            with open(ISSUES_FILE, "w") as f:
                json.dump(
                    issues_data,
                    f,
                    indent=4
                )

            response_data = issue.to_dict()
            response_data["message"] = issue.describe()

            return JsonResponse(
                response_data,
                status=201
            )

        except ValueError as e:

            return JsonResponse(
                {"error": str(e)},
                status=400
            )