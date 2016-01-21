from __future__ import absolute_import
from __future__ import unicode_literals

import collections

from teamscale_client.constants import Assessment
from teamscale_client.utils import auto_str

@auto_str
class Finding(object):
    """Representation of a finding in Teamscale.
    
    Args:
        finding_type_id (str): The type id that this finding belongs to.
        message (str): The main finding message
        assesssment (constants.Assessment): The assessment this finding should have. Default is `YELLOW`. 
                                            This value is only important if in Teamscale the finding enablement 
                                            is set to auto, otherwise the setting from Teamscale will be used.
        start_offset (int): Offset from the beginning of the file, where the finding area starts (zero-based, inclusive).
        end_offset (int): Offset from the beginning of the file, where the finding area ends (zero-based, inclusive).
        start_line (int): The finding's first line (one-based, inclusive). Can be left blank, if the offsets are given.
        end_line (int): The finding's last line (one-based, inclusive). Can be left blank, if the offsets are given.
        identifier (Optional[str]): Advanced usage! Path to special elements in Teamscale, e.g. Simulink model parts. If this is given, offsets and lines do not need to be filled.  
    """

    def __init__(self, finding_type_id, message, assessment=Assessment.YELLOW, start_offset=0, end_offset=0, start_line=0, end_line=0, identifier=None):
        self.findingTypeId = finding_type_id
        self.message = message
        self.assessment = assessment
        self.startOffset = start_offset
        self.endOffset = end_offset
        self.startLine = start_line
        self.endLine = end_line
        self.identifier = identifier

@auto_str
class FileFindings(object):
    """Representation of a file and its findings.
    
    Args:
        findings (List[:class:`Finding`]): A list containing all findings that are present in this file. 
        path (str): The path to the file in Teamscale.
        content (Optional[str]): The content of the file (can be left empty).
    """
    def __init__(self, findings, path, content=None):
        self.findings = findings
        self.path = path
        self.content = content


FindingDescription = collections.namedtuple('FindingDescriptions', ['typeid', 'description', 'enablement'])
"""Description of a finding type to be added at configuration time.

    Args:
        typeid (str): The id used to reference the finding type.
        description (str): The text to display that explains what this finding type is about (and ideally how to fix it). This text will be the same for each concrete instance of the finding.
        enablement (constants.Enablement): Describes the default enablement setting for this finding type, used when it is added to the analysis profile.
"""

class ServiceError(Exception):
    """Teamscale service returned an error."""
    pass
