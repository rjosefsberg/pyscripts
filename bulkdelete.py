import os
for root, dirs, files in os.walk("/Users/ryan/projects/simflofy/connectors"):
    for file in files:
        if file.endswith(".properties") and "test" not in root:
                os.remove((os.path.join(root, file)))