"""Write content to a text file."""

from typing import Annotated
from pydantic import BaseModel, Field

class Output(BaseModel):
    message: str

async def write_file(
    path: Annotated[str, Field(description="Full path where to write the file")],
    content: Annotated[str, Field(description="Content to write into the file")]
) -> Output:
    """Write the given content to the specified file."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return Output(message=f"Successfully wrote to {path}")
    except Exception as e:
        raise Exception(f"Error writing file: {e}")

export = write_file
