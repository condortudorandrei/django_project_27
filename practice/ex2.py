
import os
import json
from pprint import pprint
from pathlib import Path

# f = open("data.txt", "r", encoding="utf-8")
# f.close()
#58,91,121,78,98,48,108,83,119,65,78,68,115,70,117,90,81,52,71,74,118,122,50,79,69,121,53,114,69,94

# path = Path("data.txt")

class ProcessFileContent:
    def __init__(self):
        pass

    def get_file_content(self, p) -> str:
        f = open("data.txt", "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content

    def write_to_file(self, string_content, p):
        w = open(p, "w", encoding="utf-8")
        w.write(string_content)

    def process(self, p):
        content = self.get_file_content(p).split(",")
        # = f.read(p).split(",")
        result = ""
        for i_each in content:
            if i_each == "":
                continue
            each = int(i_each)
            if each > 47 and each < 127:
                if result == "":
                    result += f"{each}"
                else:
                    result += f",{each}"
        self.write_to_file(result, p)

proc = ProcessFileContent()
proc.process("data.txt")


class ProcessFileToText(ProcessFileContent):
    def process(self, p):
        content = self.get_file_content(p).split(",")
        # = f.read(p).split(",")
        result = ""
        for i_each in content:
            if i_each == "":
                continue
            each = int(i_each)
            if each > 47 and each < 127:
                if result == "":
                    result += f"{chr(each)}"
                else:
                    result += f",{chr(each)}"
        self.write_to_file(result, p)

proc2 = ProcessFileToText()
proc2.process("data.txt")