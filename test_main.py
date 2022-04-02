import main

def test_index():
    assert main.index() == f"<p>This returns the value of the index function<p>"

def test_info():
    assert main.info() == f"<p>This returns everything of the info function.<p>"

def test_contact():
    assert main.contact() == f"<p>This returns everything of the contact function.<p>"