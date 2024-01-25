def suffix_summary(path, summary):
    kv = {
        "/create": "-Create",
        "/bulk_create": "-BulkCreate",
        "/update": "-Update",
        "/refresh": "-Refresh",
        "/verify": "-Verify",
        "/reorder": "-Reorder",
        "/delete": "-Delete",
        "/bulk_delete": "-BulkDelete",
        "/publish": "-Publish",
        "/bulk_publish": "-BulkPublish",
        "/translate": "-Translate",
        "/activate": "-Activate",
        "/deactivate": "-Deactivate",
    }
    for k, v in kv.items():
        if path.endswith(k):
            if v not in summary:
                summary = summary + v
    return summary