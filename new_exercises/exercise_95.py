'''
教學：兩個物件可以各自記錄狀態；一個方法可以同時更新自己和收到的物件。

class Bell:
    def __init__(self):
        self.ring_count = 0

class Keeper:
    def __init__(self):
        self.action_count = 0

    def ring(self, bell):
        bell.ring_count += 1
        self.action_count += 1

bell = Bell()
keeper = Keeper()
keeper.ring(bell)
print(bell.ring_count, keeper.action_count)

呼叫方法後，Bell 和 Keeper 各自保留自己的計數。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 95：音樂播放器播放歌曲

定義 Song 類別，儲存歌曲名稱 title 和播放次數 play_count，初始值為 0。
定義 MusicPlayer 類別，儲存播放器名稱 name 和總播放次數 total_plays，初始值為 0。

新增 play 方法，接收一個 Song 物件：
- 每呼叫一次，歌曲的 play_count 和播放器的 total_plays 都增加 1。
- 顯示歌曲播放次數和播放器總播放次數。

在 if __name__ == "__main__": 區塊建立物件並呼叫 play。

標準輸入範例 1：

song = Song("晨光", 0)
player = MusicPlayer("客廳播放器")
player.play(song)

預期輸出 1：

晨光播放 1 次
客廳播放器總播放 1 次

標準輸入範例 2：

song = Song("星空", 0)
player = MusicPlayer("書房播放器")
player.play(song)
player.play(song)

預期輸出 2：

星空播放 2 次
書房播放器總播放 2 次
'''
