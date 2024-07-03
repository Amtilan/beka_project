from dataclasses import dataclass
import pandas as pd
import PyPDF2

@dataclass
class Filework:
    file_name: str
    file_location: str
    content: str = None
    
    def get_content(self) -> str:
        if self.file_name.endswith('.txt'):
            return self._get_text_content()
        elif self.file_name.endswith('.csv'):
            return self._get_csv_content()
        elif self.file_name.endswith('.pdf'):
            return self._get_pdf_content()
        else:
            raise ValueError("Unsupported file format")

    def _get_text_content(self) -> str:
        with open(self.file_location, 'r', encoding='utf-8') as file:
            return file.read()

    def _get_csv_content(self) -> str:
        df = pd.read_csv(self.file_location)
        return df.to_string(index=False)

    def _get_pdf_content(self) -> str:
        with open(self.file_location, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text.strip()

    def save_to_file(self, save_location: str) -> None:
        with open(save_location, 'w', encoding='utf-8') as file:
            file.write(self.content)

    def set_content(self, new_content: str) -> None:
        self.content = new_content.strip()