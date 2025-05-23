"""
This type stub file was generated by pyright.
"""

import dataclasses
import enum
from typing import Any, Callable, Sequence
from google.generativeai.notebook import model_registry
from google.generativeai.notebook.lib import llm_function, llmfn_inputs_source, llmfn_outputs, model as model_lib

"""Results from parsing the commandline.

This module separates the results from commandline parsing from the parser
itself so that classes that operate on the results (e.g. the subclasses of
Command) do not have to depend on the commandline parser as well.
"""
PostProcessingTokens = Sequence[Sequence[str]]
TextResultCompareFn = Callable[[str, str], Any]
class CommandName(enum.Enum):
    RUN_CMD = ...
    COMPILE_CMD = ...
    COMPARE_CMD = ...
    EVAL_CMD = ...


@dataclasses.dataclass(frozen=True)
class ParsedArgs:
    """The results of parsing the command line."""
    cmd: CommandName
    model_args: model_lib.ModelArguments
    model_type: model_registry.ModelName | None = ...
    unique: bool = ...
    inputs: Sequence[llmfn_inputs_source.LLMFnInputsSource] = ...
    sheets_input_names: Sequence[llmfn_inputs_source.LLMFnInputsSource] = ...
    outputs: Sequence[llmfn_outputs.LLMFnOutputsSink] = ...
    sheets_output_names: Sequence[llmfn_outputs.LLMFnOutputsSink] = ...
    compile_save_name: str | None = ...
    lhs_name_and_fn: tuple[str, llm_function.LLMFunction] | None = ...
    rhs_name_and_fn: tuple[str, llm_function.LLMFunction] | None = ...
    compare_fn: Sequence[tuple[str, TextResultCompareFn]] = ...
    ground_truth: Sequence[str] = ...


