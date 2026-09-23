# The Unofficial Guide

Yoobin Chang, Campus Life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does


The system embeds *Campus Life* corpus. It answers all the questions regarding general questions on campus life like course add/drop, meal plans, parkings. It includes information on courses (exams, workload, previous students' comments). The corpus has student's comment on certain class, housing,

## Chunking Strategy

**Chunk size:**
400 characters target
**Overlap:** 0 characters

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

I chose a 400-character target and no overlap because the campus_life corpus
contains short posts averaging about 317 characters, with most useful answers
contained in one paragraph. The chunker splits at blank-line paragraph
boundaries instead of cutting through a sentence. It attaches a short title to
the paragraph below it so a chunk does not contain only a heading. No overlap
is needed because each paragraph is kept intact and the posts are short.



## Sample Chunks

======================================================================
**Chunk 1** - source: admin_add_drop_deadline.txt#0 - produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
**Chunk 2** - source: course_biol_160.txt#0 - produced by: chunker.py::split_documents
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

======================================================================
**Chunk 3** - source: course_phys_130_workload.txt#0 - produced by: chunker.py::split_documents
======================================================================
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.

======================================================================
**Chunk 4** - source: admin_meal_plan_changes.txt#0 - produced by: chunker.py::split_documents
======================================================================
On the meal plan changes

You can change your meal plan tier once, in the first ten days of the semester. After that it's locked. Downgrading refunds the difference to your student account; upgrading bills you immediately.

======================================================================
**Chunk 5** - source: housing_innisfree_hall.txt#0 - produced by: chunker.py::split_documents
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** What is the add/drop deadline?

**Answer:**
"You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other."
Source: admin_add_drop_deadline.txt#0
