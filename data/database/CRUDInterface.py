from typing import TypeVar
T = TypeVar('T')

class CRUDInterface:

    # レコードの作成
    def create(self, item: T) -> bool:
        pass

    # 指定したidのレコードを更新
    def update(self, item: T) -> bool:
        pass

    # テーブルデータの取得
    def read(self, id: int) -> T:
        pass

    # 指定したidのレコードを削除
    def delete(self, id: int) -> bool:
        pass