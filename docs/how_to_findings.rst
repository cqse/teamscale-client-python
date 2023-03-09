How to add arbitrary external findings to Teamscale using the Python API
========================================================================

Adding new Findings to Teamscale is comprised of 4 Steps:

.. contents::
   :local:

Steps 1-3 are one-time setup tasks, whereas 4 will be repeated every time new findings shall be added.

Add a new findings group
------------------------
First a new group has to be created. A group contains multiple different types of (usually related) 
finding types. A group can be created like this:

..  code-block:: python

    client.add_findings_group("Finding Group 1", "external-findings-.*")

The Group has a name that will be visible in the Teamscale UI (for example as a filter in the Findings View). The regex will be used to find all matching finding descriptions that shall be grouped under the given name.

.. image:: _static/images/findings-filter.png

Add a finding description
-------------------------
For each type of finding that is to be uploaded, a new :any:`FindingDescription` must be added. A description is comprised of an id
that is used to identify the type of finding, a description that is displayed whenever a finding of this type
is shown in detail and a default enablement/severity.

Finding descriptions can be added like this:

..  code-block:: python

    descriptions = [
        FindingDescription("externals-1", "A test finding description", Enablement.RED, "externals-1"),
        FindingDescription("externals-2", "Another finding description", Enablement.YELLOW, "externals-2")
    ]
    response = client.add_finding_descriptions(descriptions)


Update the analysis profile
---------------------------
The third step is updating the analysis profile used by the profile. Either create a new profile or edit an existing profile.
When editing the profile enable the ``Custom External Findings`` external tool in the external tools step of the analysis profile wizard.

The created finding groups will then be available as analysis group. They are grouped under the quality indicator ``Code Anomalies`` by default.

.. image:: _static/images/analysis-profile.png

These can be edited to override the default enablement or deactivated completely.

Save the analysis profile. 

In case the profile references existing projects that use this profile, you can enable the expert settings in the ``Project re-analysis required`` dialog 
and enable ``Only Schema update`` for the required projects.

.. image:: _static/images/re-analysis-required.png


Upload the findings
-------------------
In the last step, you upload any number of concrete :any:`Finding` instances for each file (see also :any:`FileFindings`) using ids from the previously created finding descriptions:

..  code-block:: python

    findings = [
        FileFindings([
            Finding("externals-1", "test2", start_line=3,
                    finding_properties={"someStringProperty": "severe", "someNumericProperty": 42.0})
        ],
            "src/Foo.java")
    ]
    response = client.upload_findings(findings, "TestCommit", "test-partition", timestamp=datetime.datetime.now())

If everything worked you should be able to see the new finding and the details will be shown:

..  image:: _static/images/finding-detail.png
