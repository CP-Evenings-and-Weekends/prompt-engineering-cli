# Prompt Comparison

## Use Case

API Endpoint Designer

## Poorly Written Prompt

Make API endpoints for Book.

Prompt is vague. It doesn't tell the model what role to take, what
ops are needed, what fields the resource contains, or how the response
should be formatted.

## Engineered Prompt

Tells the model that it's an API designer specializing
in RESTful APIs. Provides the resource name, fields, and requested
operations.

Example input:

Resource: Book  
Fields: title, author, published_date  
Operations: CRUD

The prompt requires each endpoint to use this format:

Method:  
Path:  
Purpose:

It also provides a Student API example and separates the user's resource data
with `### RESOURCE START ###` and `### RESOURCE END ###` delimiters.

## Prompt Engineering Techniques Used

1. **System Prompt** - Gives model the role of a REST API designer and
   establishes constraints for response.
2. **Few-Shot Prompting** - Provides a Student API example showing the model
   what a correct response should look like.
3. **Structured Output and Specificity** - Requires every endpoint to contain
   Method, Path, and Purpose.
4. **Delimiters** - Separates user-provided resource info from the
   instructions.

## Comparison

The poorly written prompt only asks the model to make API endpoints, leaving
the model to decide the structure, conventions, and amount of detail. The
engineered prompt is more specific and predictable because it defines the
model's role, provides an example, separates the input from the instructions,
and requires a consistent output format. These techniques should make the
response easier to use and reduce ambiguity.