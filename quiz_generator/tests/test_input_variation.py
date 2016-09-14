"""
Tests for Variation class
"""
import itertools

from quiz_generator.input_variation import Variation

def test_sequential_variation_storage():
    """Test that variation is able to be stored in a sequentially accessible manner"""
    items = ["a", "b", "c"]
    variation = Variation(items, selection_method=Variation.SEQUENTIAL)
    generated = variation.get()
    assert all(a == b for a, b in itertools.zip_longest(generated, items))
