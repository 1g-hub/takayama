# coding: utf-8
import MeCab

ori = ['A', '?', 'DVD', 'B', '!', 'GPU', '2', '.']
aug = ['A', '毎毎', '日夕', '常住坐臥', '斯うして', '迚も', '其は其は', '其れは其れは', '斯く', '寔に', '悉皆', '頗る', '斯う', '田仮', '憩', '田假', '一時停止', '少憩', '小憩', '憩い', '?', '秘訣', '色艶', '恰好', '粧い', '膚色', '顏', '佞悪', '無惨', '兇悪', '姦譎', '遺憾', '拙劣', '拙い', '面貌', '下手糞', '奸譎', '相貌', '悪辣', 'DVD', 'B', '瀟洒', '窈窕たる', '優艶', '雅馴', '嬋媛', '優婉', '修訂', '校閲', '更訂', '是正措置', '悍ましい', '物凄まじい', 'もの恐ろしい', '物恐ろしい', '物凄い', '悍ましげ', '絵姿', '!', '婉美', '艷やか', '可憐', '明媚', '風光明媚', '眩い', '贔屓', '贔負', '愛顧', '恩顧', '令閨', '嚊', 'まっ只中', '嬶', '真っ只中', '真只中', '灑掃', '洒掃', '洗滌', '渫う', '嚊左衛門', '浚う', '凡愚', '臍', '年嵩', '査閲', '婢', '下婢', '気慰み', '嘱目', '謂われ因縁', '謂れ', '謂れ因縁', '謂われ', '御饒舌', '述', 'お喋り', '御喋り', '進呈', '恤む', '婬奔', '濫りがわしい', '猥りがましい', '婬靡', '淫靡', '妄りがましい', '濫りがましい', '猥りがわしい', '淫奔', '妄りがわしい', 'GPU', '形姿', '山橘', '芍薬', '形貌', '態', '辯論', '僉議', 'もの恐ろしさ', '物恐ろしさ', '惧れ', '愉しげ', '愉しい', '心嬉しい', '愉快', '措辞', '単語の選択', 'o.k.', '心肝', '尤も', '精緻', '稟質', '旨趣', '稟賦', '気稟', '稟性', '禀性', '下僕', '家僕', '傍輩', '頓に', '豁然', '儷', '侶伴', '同侶', '儕', '伴侶', '侶', '急激', '颯と', '俄に', '忽ち', '俄然', '忽然', 'vol.', '巻帙', '-冊', '篇帙', '根柢', '拝誦', '披見', '繙く', '閲読', '繙読', '書帙', '竹帛', '述作', '纔か', '心做しか', '却々', '稍', '聊か', '芥もくた', '咎', '疵', '搦め手', '瑕疵', '疵瑕', '嫌厭', '小面憎さ', '搦手', '蒼穹', '蒼昊', '稗官', '実践躬行', '当て嵌める', '逐って', '輓近', '今日此の頃', '今日此頃', '2', '大凡', '殆', '粗粗', '何が何でも', '何でも彼でも', '非凡', '希覯', '稀覯', '奇矯', '超凡', '希覯さ', '相討', 'チョコレート飲料', '一個', '壱', '殊更', '殊に', '擯斥', '扣除', '除斥', '洩らす', '発兌', '壟断', '因果関係', '優渥', '慈悲深い', '耀かしい', '尤', '絶巧', '皆乍', '皆乍ら', '壱に', '完膚なきまで', '完膚なきまでに', '完膚無き迄に', '頓と', '満更', '完膚無き迄', '持堪える', '持ち堪える', 'ちかぢか', '頓て', '軈て', '孰れ', '已に', '.', '暫時', '気恥ずかしい', '腑甲斐ない', '心疚しい', '心疾しい']
mecabTagger = MeCab.Tagger("-Ochasen")
mecabTagger.parse('')
hcount = {}

for w in aug:
    node = mecabTagger.parseToNode(w)

    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in hcount.keys():
            freq = hcount[hinshi]
            hcount[hinshi] = freq + 1
        else:
            hcount[hinshi] = 1
        node = node.next
for key,value in hcount.items():
    print(key+":"+str(value))