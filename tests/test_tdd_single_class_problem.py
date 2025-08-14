from lib.tdd_single_class_problem import DiaryEntry
import pytest 

def test_format_of_entry():
    new_diary = DiaryEntry("Hello", "This is a new entry")
    result = new_diary.format() 
    assert result == "Hello: This is a new entry"

def test_word_count():
    new_diary = DiaryEntry("Hello", "This is a new entry")
    result = new_diary.count_words()
    assert result == 6

def test_empty_word_count():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Diary must have title or contents"

def test_wpm_method_with_nonzero():
    new_diary = DiaryEntry("Hello", "This is a new entry and I love books ")
    assert new_diary.reading_time(10) == 1

def test_wpm_method_with_zero():
    new_diary = DiaryEntry("Hello", "This is a new entry and I love books ")
    with pytest.raises(Exception) as e:
        new_diary.reading_time(0)
    assert str(e.value) == "You cant read"