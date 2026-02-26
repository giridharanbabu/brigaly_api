def build_prompt(title: str, content: str, content_type: str) -> str:
    return f"""
You are a strict academic content reviewer and compliance analyst.

Review the following {content_type}.

Title: {title}

Content:
\"\"\"
{content}
\"\"\"

Evaluate:

1. clarity_score (0-10)
2. structure_score (0-10)
3. grammar_score (0-10)
4. tone (short description)
5. tone_match (true/false)

6. plagiarism_risk_score (0-10)
7. plagiarism_notes (list reasons)

8. misleading_claims (list)
9. exaggerated_statements (list)
10. unverified_statements (list)

11. education_alignment_score (0-10)
12. audience_relevance_score (0-10)

13. improvement_suggestions (list)
14. suggested_headline (string)
15. suggested_summary (2-3 sentences)
16. suggested_tags (list)
17. rewritten_sample (3-5 improved sentences)

IMPORTANT:
Return ONLY valid JSON.
No markdown.
No explanations.

Schema:
{{
  "clarity_score": 0,
  "structure_score": 0,
  "grammar_score": 0,
  "tone": "",
  "tone_match": true,
  "plagiarism_risk_score": 0,
  "plagiarism_notes": [],
  "misleading_claims": [],
  "exaggerated_statements": [],
  "unverified_statements": [],
  "education_alignment_score": 0,
  "audience_relevance_score": 0,
  "improvement_suggestions": [],
  "suggested_headline": "",
  "suggested_summary": "",
  "suggested_tags": [],
  "rewritten_sample": ""
}}
"""