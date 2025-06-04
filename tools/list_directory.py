"""List contents of a directory."""

from typing import Annotated, List
from pydantic import BaseModel, Field
import os

class Output(BaseModel):
    """List of directory contents."""
    entries: List[str]

async def list_directory(
    path: Annotated[str, Field(description="Path to the directory")]
) -> Output:
    """List the contents of the specified directory."""
    try:
        entries = os.listdir(path)
        return Output(entries=entries)
    except Exception as e:
        raise Exception(f"Error listing directory: {e}")

export = list_directory