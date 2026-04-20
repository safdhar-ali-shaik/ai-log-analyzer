def analyze_log(log):
    log = log.lower()

    if "error" in log:
        if "auth" in log or "authenticate" in log:
            return {
                "type": "AUTH_ERROR",
                "severity": "HIGH",
                "message": log,
                "suggestion": "Check authentication token or login flow"
            }

        elif "not found" in log:
            return {
                "type": "NOT_FOUND",
                "severity": "MEDIUM",
                "message": log,
                "suggestion": "Check API endpoint or routing"
            }

        else:
            return {
                "type": "GENERAL_ERROR",
                "severity": "HIGH",
                "message": log,
                "suggestion": "Investigate service logs"
            }

    elif "warn" in log:
        return {
            "type": "WARNING",
            "severity": "LOW",
            "message": log,
            "suggestion": "Monitor this warning"
        }

    else:
        return {
            "type": "INFO",
            "severity": "LOW",
            "message": log,
            "suggestion": "No action needed"
        }