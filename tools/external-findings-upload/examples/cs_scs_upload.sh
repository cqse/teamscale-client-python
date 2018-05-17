#!/usr/bin/env bash
export PYTHONPATH=$(cd ../../../; pwd)

# upload the group descriptions
python3 ../upload_group_description.py ts_config cs_group_desc.json
python3 ../upload_group_description.py ts_config scs_group_desc.json

# upload the findings descriptions
python3 ../upload_finding_descriptions.py ts_config cs_findings_desc.json
python3 ../upload_finding_descriptions.py ts_config scs_findings_desc.json
