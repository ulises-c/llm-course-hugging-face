# LLM Course - Hugging Face

https://huggingface.co/learn/llm-course

## Hugging Face - Santa Clara University

https://huggingface.co/nlpscu

## Running Code Locally

Poetry is used to set up the environment, in notebooks `import sys` is required to use the virtual environment.

System Hardware Requirements

### macOS (M-Series)
1. Minimum: Apple M1 or newer with 8 GB unified memory for basic course exercises, small model inference, and notebook use.
2. Recommended for early chapters: Apple M1/M2/M3 with 16 GB unified memory for Jupyter notebooks, Transformers examples, and small model inference.
3. Real-world note: On an Apple M1 with 16 GB unified memory, the Chapter 1 notebook can still hit memory pressure and heavy swap usage when larger models are loaded. In testing, `python3.12` reached about 14.79 GB in Activity Monitor.
4. Recommended for larger local experiments: 24 GB or more unified memory if you plan to run text-generation models in the multi-billion-parameter range, keep multiple notebooks open, or work with larger datasets.
5. GPU note: Apple Silicon includes an integrated GPU that PyTorch can use through Metal Performance Shaders (MPS). Because memory is unified, GPU workloads also consume the same system memory pool.
6. Practical guidance: 16 GB is workable for the introductory material, but 24 GB or more is a safer target if you want to run larger local models comfortably without relying on swap.
7. Storage: Keep at least 10-20 GB of free disk space for the Python environment, notebook artifacts, downloaded models, and dataset caches.

### Personal Computer
1. Minimum: Modern 4-core CPU, 8 GB RAM, and no dedicated GPU if you only plan to run introductory exercises and small inference examples.
2. Recommended: 16 GB RAM for a more comfortable local workflow with Poetry, Jupyter, Transformers, and cached datasets/models.
3. NVIDIA GPU recommendation: 8 GB VRAM is a good starting point for faster inference and small training jobs; 12-24 GB VRAM is better for fine-tuning and larger local experiments.
4. CPU-only note: The course can be started without a GPU, but execution will be slower and some larger experiments may be impractical locally.
5. Storage: Keep at least 10-20 GB of free disk space, with more space needed if you download multiple models or work with larger datasets.

## Chapter 0 - Setup

https://huggingface.co/learn/llm-course/chapter0/1

## Chapter 1 - Transformer Models

https://huggingface.co/learn/llm-course/chapter1/1

# Extra Resources

## Useful Resources for the LLM Course

1. Practical Deep Learning for Coders
   1. https://course.fast.ai/
2. DeepLearning
   1. https://www.deeplearning.ai/

## Further Learning

1. DeepLearning.AI’s Natural Language Processing Specialization
   1. https://www.coursera.org/specializations/natural-language-processing

## Code Repositories

1. https://github.com/huggingface/notebooks
2. https://github.com/huggingface/course#-jupyter-notebooks
