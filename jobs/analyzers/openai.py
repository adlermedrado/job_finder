import logging

from openai import OpenAI

logger = logging.getLogger(__name__)


class JobAnalyzer:
    def __init__(self, api_key, model='gpt-4o-mini', max_tokens=200, temperature=0.5):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def analyze_job_description(self, job_description):
        prompt = (
            'Analyze the job description based on the following criteria: '
            '1. Remote Work: Check if the job is 100% remote. Internally determine whether it "Fully meets", "Partially meets", or "Does not meet". '
            '2. Technologies: Check if the listed technologies (PHP, Java, Python) are mentioned in the job description. Internally determine whether it "Fully meets" or "Does not meet". '
            '3. Employment Model: Verify if the employment model is specified as CLT or PJ. If the job is PJ, internally determine it as "Fully meets". If CLT, determine it as "Partially meets". Otherwise, determine it as "Does not meet". '
            '4. Job Level: Check if the job is listed as Senior level or above (e.g., Senior, Lead, Principal). If the job explicitly mentions Senior level or above, respond with "Fully meets". Otherwise, determine it as "Does not meet". '
            'After evaluating these criteria, respond with only one of the following based on the overall analysis: '
            '- "Fully meets" if all criteria meet this level. '
            '- "Partially meets" if at least one criterion is partially met. '
            '- "Does not meet" if none of the criteria meet the expectations. '
            'Return only the final result without additional explanations.'
        )
        payload = {
            'model': self.model,
            'messages': [
                {
                    'role': 'system',
                    'content': prompt,
                },
                {'role': 'user', 'content': job_description},
            ],
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
        }

        try:
            response = self.client.chat.completions.create(**payload)
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f'Error during API call: {e}')
            return None
