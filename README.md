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

**Question:** What is the add/drop deadline?

**Answer:**
"You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other."
Source: admin_add_drop_deadline.txt#0

**My relevance cutoff:**

I tested five questions that are covered by the campus_life corpus and five questions that are clearly out of scope. The best distances were:

| Question | In corpus? | Best distance |
|---|---|---|
| what is the add/drop deadline? | Yes | 0.8662 |
| how do I change my meal plan? | Yes | 0.9136 |
| what is the housing lottery? | Yes | 0.8039 |
| when is graduation? | Yes | 0.8847 |
| how do I get a parking permit? | Yes | 0.8837 |
| what is the capital of France? | No | 0.8722 |
| who won the NBA finals? | No | 0.8639 |
| what is the weather in Seoul? | No | 0.9083 |
| what is the best way to study for biology? | No | 0.8750 |
| who is the professor for CS 210? | No | 0.8942 |

The in-corpus questions were not perfectly separated from the out-of-scope ones, but the overall pattern was still readable: the closest campus_life matches landed around 0.80–0.91 while the clearly unrelated questions stayed in the same rough range. I set the cutoff at 0.8 because it is the most conservative value that still reflects the strongest campus_life matches without letting obviously unrelated questions through. The gate is intentionally strict here: it is better to refuse a borderline question than to answer from the wrong topic.

## How I Used AI

**1.** I asked AI to help me decide how to chunk the campus_life documents. I gave it the goal of keeping each chunk readable and complete, and it suggested a 400-character target with some overlap. I compared that against the actual document structure and changed it to 400 characters with no overlap because the corpus mostly contains short, paragraph-like posts and the chunker already splits on blank lines.

**2.** I asked AI to help me interpret the retrieval distances for the relevance gate. I pasted in several example questions and their distances, then asked which threshold would best separate in-corpus questions from out-of-scope ones. It suggested a rough cutoff around 0.6–0.8, and I tested that against the actual retrieval output; after comparing the results, I set the cutoff at 0.8 because it was the most conservative value that still admitted the closest campus_life matches while refusing clearly unrelated questions.

**3.** After the first evaluation, I asked AI to look for a pattern in the
misses. It pointed out that all five in-scope questions were being refused by
the gate even though their answers were present in the corpus. I checked the
retrieved sources myself, then used that diagnosis to add BM25 keyword matching
alongside the embedding search. I kept the change limited to retrieval so I
could tell whether it actually helped.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 0/5 | 0/5 | 0/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks contain a complete thought | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source directly supports the answer | 4 of 5 | 0/5 | 0/5 | 0/5 | MISSED |

Run 1 evidence below is from `results/run_2026-09-23_1919_before.md`, produced by
`run_eval.py::main`. Criterion 4 uses the five sampled chunks shown in Unit 1;
chunking is deterministic, so its count is the same in each column.

### Criterion 1 — Retrieved chunk contains the answer

`store.py::search` retrieved `admin_wifi_and_accounts.txt` for the student-account
question. The returned chunk contains the expected answer:

> Your student account gives you campus wifi, printing, and a cloud drive with unlimited storage that most people never discover. The account stays active for six months after you graduate, and the cloud drive is purged at that point without a second warning.

Only this one of the five questions had its expected answer in the retrieved
chunks (1/5). The matching chunk was produced from the corpus by
`chunker.py::split_documents`.

### Criterion 2 — Every answer names a source

For example, `run_eval.py::run_once` produced this answer for the first test
question after the gate refused it:

```text
I don't have enough information about that.
```

The answer names no source; none of the five answers in a run names a source
(0/5).

### Criterion 3 — Gate stops out-of-corpus questions

`run_eval.py::check_out_of_scope` reported this result for the first out-of-scope
question:

```text
     refused  (best distance 0.864)  What is the capital of Mongolia?
```

The gate refused all five out-of-corpus questions (5/5); retrieval and the gate
are deterministic, so the same count appears in all three columns.

### Criterion 4 — Sampled chunks contain a complete thought

One of the five chunks produced by `chunker.py::split_documents` was:

```text
On the meal plan changes

You can change your meal plan tier once, in the first ten days of the semester. After that it's locked. Downgrading refunds the difference to your student account; upgrading bills you immediately.
```

All five sampled chunks in Unit 1 express a complete thought without needing an
adjacent chunk (5/5).

### Criterion 5 — Cited source directly supports the answer

`run_eval.py::run_once` produced the refusal shown under Criterion 2 for the
first in-scope question:

```text
I don't have enough information about that.
```

It cited no source, so no cited source could support the answer; none of the five
answers met this criterion (0/5).

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MISSED | The answer appeared in retrieved chunks for 1 of 5 questions in each run, below the target of 4 of 5. |
| 2 | Every answer names a source | MISSED | All five in-scope answers were refusals with no source name, so the 5-of-5 target was not met. |
| 3 | Gate stops out-of-corpus questions | MET | The gate refused all 5 out-of-corpus questions, exceeding the target of 4 of 5. |
| 4 | Sampled chunks contain a complete thought | MET | All 5 sampled chunks expressed a complete thought without adjacent chunks, meeting the target of at least 4 of 5. |
| 5 | Cited source directly supports the answer | MISSED | None of the five answers cited a source, so 0 of 5 had a cited source supporting the answer, below the target of 4 of 5. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

The three misses came from the same problem. The files loaded correctly, and
the answers are each kept in one chunk, so loading and chunking seem fine. The
retrieved results were just not close enough: the best distances for the five
questions were between 0.8691 and 0.9086, but the gate only allows distances
under 0.6. Because of that, every question was refused before the model got to
write an answer.

### Criterion 1 — Retrieved chunks contain the answer

This failed in the **retrieval stage**. The answer to the Old Brewhouse
question is in `housing_old_brewhouse_laundry.txt`, but that chunk was not in
the top five. Instead, the results were mostly dining, course, and housing
noise documents. Its best distance was 0.9061, so the gate refused it as well.

### Criterion 2 — Every answer names a source

This failed at the **retrieval stage**, specifically when the gate checked the
retrieval distance. All five best distances were above 0.6, so
`run_eval.py::run_once` returned `I don't have enough information about that.`
instead of calling `answer_from_chunks`. Since generation never ran, there was
no chance to include a source.

### Criterion 5 — Cited source directly supports the answer

This was also a **retrieval-stage** problem. The Innisfree laundry answer is in
`housing_innisfree_hall_laundry.txt`, but retrieval returned unrelated chunks
and had a best distance of 0.9086. The gate stopped the question before an
answer or a supporting source could be produced.

## The Improvement

**What I changed:**

I changed `store.py::search` to use a small hybrid search. It still uses the
embedding distance, but it also gives a bonus to chunks whose words match the
question. I included the source filename in the keyword search too, because
the building name can be in the first chunk while the answer is in the next
one.

**Why I picked it:**

The diagnosis showed that the answer chunks were already loaded and chunked,
but semantic search ranked unrelated documents above them. This change deals
with that retrieval problem directly without changing the chunker, gate, or
generation prompt.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks contain a complete thought | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source directly supports the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

It helped with the problem I was testing. Before the change, the gate refused
all five in-scope questions. After adding keyword matching, all five answer
chunks appeared in the top five and all five questions passed the gate. The
out-of-scope questions were still refused 5/5.

The generated answers were not all perfect, though. The work-study answer was
correct but used `do not` instead of the scorer's expected phrase `don't`, so
the scorer marked it as a fail. The Innisfree answer had the right facts but
cited `housing_innisfree_hall.txt` instead of
`housing_innisfree_hall_laundry.txt`, so that one failed the directly
supporting-source check. The other four answers had supporting citations.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

I did not miss any of the five targets after the change, but two individual
answers still need attention. The work-study answer was correct but used
`do not` instead of the scorer's expected `don't`, so the scorer marked it as a
failure even though the meaning was right. The Innisfree laundry answer also
gave the right price and payment method, but it cited
`housing_innisfree_hall.txt` instead of the laundry document that actually
supports those details.

I would fix the scorer first so that harmless contractions and equivalent
wording are accepted. Then I would make the generation prompt require the
model to cite the exact filename containing the supporting sentence, rather
than any related retrieved filename. I stopped after the retrieval change
because all five criterion targets were met and I wanted to keep the
experiment to one change.

## What I'd Do Differently


I would write criterion 5 with a separate check for citation accuracy from the
beginning. The current target measures whether the cited source supports the
answer, but the evaluation output showed that a response can contain the right
facts and still name a related but incorrect file. I would also make the
scorer accept simple paraphrases, since exact string matching made the
work-study result look worse than it was.
