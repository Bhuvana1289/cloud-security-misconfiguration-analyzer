def analyze_config(config):
    issues = []
    recommendations = []

    if config.get("bucket") == "public":
        issues.append("S3 Bucket is PUBLIC")
        recommendations.append("Make bucket private")

    if not config.get("encryption"):
        issues.append("Encryption is DISABLED")
        recommendations.append("Enable encryption for data safety")

    if "ports" in config:
        if 22 in config["ports"]:
            issues.append("Port 22 (SSH) is OPEN")
            recommendations.append("Restrict SSH access")

    if config.get("admin_access"):
        issues.append("Admin access is ENABLED")
        recommendations.append("Use least privilege access")

    return issues, recommendations
