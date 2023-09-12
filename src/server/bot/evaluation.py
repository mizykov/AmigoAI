from sentence_similarity import sentence_similarity


SSM = "sentence-transformers/all-MiniLM-L6-v2"


class Scorer:
    def __init__(self, embedding_type="cls_token_embedding"):
        self.model = sentence_similarity(model_name=SSM, embedding_type=embedding_type)

    def messure_score(self, first_sentence=str, second_sentence=str, metric="cosine") -> float:
        score = self.model.get_score(first_sentence, second_sentence, metric=metric)
        return score
