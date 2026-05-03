class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str, text_2 = None):
        if text_2 is None:
            return text1.upper()
        return text1+text_2
    


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
