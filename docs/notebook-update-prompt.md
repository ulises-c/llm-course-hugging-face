# Prompt: Update HuggingFace Course Notebooks for Local Use

Use this prompt when updating a new chapter's notebooks. Paste it into a Claude Code session after opening the repo.

---

## Prompt

Update Chapter N notebooks (`src/llm_course_hugging_face/chapterN/`) to run locally with the current API. The notebooks were originally written for Google Colab against older versions of `transformers`, `huggingface_hub`, and `accelerate`.

**Use chapters 3–6 as the reference for what "done" looks like.** Ch4/4_3 and Ch6/6_8 are particularly good examples. Give less weight to ch1–2 since they predate some of the fixes.

### Rules

#### Always apply

| Location                        | Old (Colab/outdated)                                                          | New (local/current)                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Install cell                    | `!pip install ...` / `!apt install git-lfs`                                   | Comment out with `# Local environment — packages already installed.` header                          |
| Git config cell                 | `!git config --global ...`                                                    | Comment out                                                                                          |
| Duplicate `notebook_login()`    | Second (and any further) call                                                 | Remove — keep only the first                                                                         |
| `TrainingArguments`             | `evaluation_strategy=`                                                        | `eval_strategy=`                                                                                     |
| `Trainer` / `Seq2SeqTrainer`    | `tokenizer=tokenizer`                                                         | `processing_class=tokenizer`                                                                         |
| `TrainingArguments`             | `fp16=True`                                                                   | `bf16=True`                                                                                          |
| `Accelerator(fp16=True)`        | —                                                                             | `Accelerator(mixed_precision="bf16")`                                                                |
| AdamW import                    | `from transformers import AdamW`                                              | `from torch.optim import AdamW`                                                                      |
| Hub repo name                   | `get_full_repo_name(model_name)`                                              | `f"{HfApi().whoami()['name']}/{model_name}"`                                                         |
| Hub repo creation               | `Repository(output_dir, clone_from=repo_name)`                                | `create_repo(repo_name, exist_ok=True)` + `os.makedirs(output_dir, exist_ok=True)`                   |
| Hub push in training loop       | `repo.push_to_hub(commit_message=..., blocking=False)`                        | `upload_folder(folder_path=output_dir, repo_id=repo_name, commit_message=...)`                       |
| Accelerate save                 | `unwrapped_model.save_pretrained(output_dir, save_function=accelerator.save)` | Add `is_main_process=accelerator.is_main_process` and `state_dict=accelerator.get_state_dict(model)` |
| ROUGE scores (evaluate 0.4+)    | `result[key].mid.fmeasure * 100`                                              | `result[key] * 100` (plain float)                                                                    |
| `distutils.dir_util.copy_tree`  | —                                                                             | `shutil.copytree(..., dirs_exist_ok=True)` (distutils removed in Python 3.12)                        |
| Extra pip installs mid-notebook | `!pip install seqeval`, `!pip install sacrebleu`, etc.                        | Comment out                                                                                          |
| NLTK downloads                  | `nltk.download("punkt")`                                                      | Also add `nltk.download("punkt_tab")` (required in NLTK 3.9+)                                        |

#### Intentionally broken cells — do NOT fix

Chapter 8 (and any debugging-focused section) contains cells that are _meant_ to fail in order to teach debugging. If a cell has an error output that the surrounding text explains, leave the bug intact. Add a comment `# Intentional error — see course text` only if the cell gives no indication it's supposed to fail.

To confirm whether an error is intentional: read the surrounding markdown cells. If they describe the error and walk through debugging it, the cell is pedagogical.

#### push_to_hub

Keep `push_to_hub=True` in `TrainingArguments` and keep `trainer.push_to_hub()` calls. This lets you track training progress on the Hub. Authentication is handled by `notebook_login()` at the top.

#### bf16 vs fp16

`bf16` is preferred for training on modern hardware (NVIDIA Ampere/Ada/Blackwell, AMD RDNA3/RDNA4). Same speed, better numerical stability (no loss scaler needed, same dynamic range as fp32).

### Questions to ask before starting

1. Are there any notebooks in this chapter that are already updated? (Check git log or compare cell content against the Colab originals.)
2. Does this chapter have a debugging section with intentionally broken cells? If yes, identify which cells should stay broken before editing.
3. Are there any chapter-specific pip installs beyond the standard set (e.g. `rouge_score`, `sacrebleu`, `seqeval`, `nltk`)? These should all be commented out.

### Verification after editing

Run these greps and confirm zero hits:

```bash
# Should be empty
grep -rn "get_full_repo_name\|from huggingface_hub import Repository\| = Repository(" src/llm_course_hugging_face/chapterN/

# Should be empty
grep -rn "evaluation_strategy=\|fp16=True\|Accelerator(fp16\|from transformers import AdamW" src/llm_course_hugging_face/chapterN/

# Should only appear in modern save_pretrained pattern (with state_dict= beside it)
grep -rn "save_function=accelerator" src/llm_course_hugging_face/chapterN/
```
