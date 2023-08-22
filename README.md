# Headshot Sheet Creation Tool

Takes images submitted by students (typically in an intro survey) and compiles a MS Word DOCX file with ttheir names and headshots. Uses `cv2` to attempt to find and extract faces, and `PIL` to resize them.

Issues:
- Method seems about 70% reliable, requiring manual corrections.
- Doesn't currently account for formats other than JPG / JPEG.
- Hard-coded paths.
