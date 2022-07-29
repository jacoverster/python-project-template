FROM python:3.9

RUN pip install --upgrade pip
COPY . .
RUN pip install .[dev]

ENV PYTHONPATH "${PYTHONPATH}:/workspaces/python-project-template"

CMD ["/bin/bash"]
