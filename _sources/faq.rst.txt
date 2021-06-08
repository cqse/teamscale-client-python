Frequently Asked Questions
==========================

.. _faq-partition:

What is the `partition` parameter used for?
-------------------------------------------

A partition denotes a `set of findings/metrics/architectures/non-code-metrics` uploaded in one session. The data present (or not present) in the upload into a partition will be used to determine if each finding/metric/etc. is old, new or has been deleted. 

Partition ids must be unique within a project, independent of the uploaded content. It is important that even if you upload metrics in one call and findings in another, that partitions must not overlap!

If you only have one place where you upload data, you can always use the same partition. If you have multiple uploads (e.g. results of tool1 are uploaded from build-slave1 and tool2's results are uploaded from build-slave2, you will want to use a different partition for each upload. By doing this, Teamscale knows that when you are uploading tool1's results, which do not contains tool2's results, that the findings from tool2 are not to be marked as deleted (since they are stored in a separate partition). 

A simple way to think about this, is that the findings are stored into different buckets, each containing a certain set of findings. If the items in each individual bucket are updated, the difference to the previous version can be calculated without affecting any items from other buckets.

Therefore: Use a separate partition for every distinct tool/server upload you are doing, but use the same partition name every time for each upload of a newer version of the same distinct tool/server.

.. _faq-offsets:

If I provide offset information with a finding, how does Teamscale handle newlines to figure out where exactly the offset points at?
------------------------------------------------------------------------------------------------------------------------------------
Teamscale assumes UNIX linebreaks. Currently, there is no way to override this. Mostly, Teamscale will figure out the correct position, as offsets are aligned to token boundaries.

