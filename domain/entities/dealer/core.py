from .details import DealerDetails


class Dealer:
    def __init__(self, details: DealerDetails) -> None:
        self.__details = details

    @property
    def health(self) -> int:
        return self.__details.health

    @property
    def intelligence(self) -> int:
        """ディーラーの賢さを取得"""
        return self.__details.intelligence

    def decide_action(self):
        """
        賢さに基づいてディーラーの行動を決定する。
        - 賢さが低い: ランダムな行動
        - 賢さが中: プレイヤーの状態を見て行動
        - 賢さが高い: 最適な行動を選択する
        """
        if self.intelligence == 1:
            # 賢さが低い -> ランダムな行動（実装例）
            return "ランダム行動"
        elif self.intelligence == 2:
            # 賢さが中 -> 状況を考慮した行動（実装例）
            return "状況に応じた行動"
        elif self.intelligence == 3:
            # 賢さが高い -> 最適な行動（実装例）
            return "最適な行動"
        else:
            return "デフォルト行動"
