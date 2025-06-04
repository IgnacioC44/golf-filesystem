"""Read the contents of a text file."""

from typing import Annotated
from pydantic import BaseModel, Field

class Output(BaseModel):
    content: str

async def read_file(
    path: Annotated[str, Field(description="Full path to the file")]
) -> Output:
    """Read and return the contents of the specified text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return Output(content=content)
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

export = read_file
