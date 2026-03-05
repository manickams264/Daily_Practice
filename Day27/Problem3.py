class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_cards = len(cardPoints)
        total_score = sum(cardPoints)
        if total_cards == k:
            return total_score
        window_size = total_cards - k
        current_window_sum = sum(cardPoints[:window_size])
        minimum_window_sum = current_window_sum
        for index in range(window_size, total_cards):
            current_window_sum += (
                cardPoints[index] - cardPoints[index - window_size]
            )
            minimum_window_sum = min(minimum_window_sum, current_window_sum)
        return total_score - minimum_window_sum
