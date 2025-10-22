import os
from flask import abort, send_file

def fetch_cv_pdf(first_name: str, last_name: str):
    """
    Returns the PDF path for the given person.
    Raises 404 if the file does not exist.
    """
    filename = "Google.pdf"  # TODO f"{first_name.lower()}_{last_name.lower()}.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), '..', '..', filename)
    pdf_path = os.path.abspath(pdf_path)

    if not os.path.exists(pdf_path):
        abort(404, description=f"CV not found for {first_name} {last_name}")

    return send_file(pdf_path, mimetype='application/pdf')

