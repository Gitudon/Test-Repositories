#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <openssl/md5.h>
using namespace std;

const int PASSWORD_SPACE = 10000; // 0000 ~ 9999 の10,000通り
const int CHAIN_LEN = 100;        // チェインの長さ (t)
const int TABLE_SIZE = 300;       // テーブルの行数 (m)

// MD5ハッシュを計算して16進数文字列を返す関数
string md5(const string &str)
{
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5(reinterpret_cast<const unsigned char *>(str.c_str()), str.length(), digest);
    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
    {
        ss << hex << setw(2) << setfill('0') << static_cast<int>(digest[i]);
    }
    return ss.str();
}

// ハッシュ文字列の先頭を数値に変換する補助関数
unsigned long long hash_to_long(const string &hash)
{
    stringstream ss;
    ss << hex << hash.substr(0, 16); // 先頭16文字(64ビット分)を切り出し
    unsigned long long val = 0;
    ss >> val;
    return val;
}

// 縮約関数 (Reduction Function: R_i)
// ハッシュ値と現在の「ステップ数」から、4桁の数字文字列を生成する
string reduce(const string &hash, int step)
{
    unsigned long long val = hash_to_long(hash);
    int num = (val + step) % PASSWORD_SPACE;
    stringstream ss;
    ss << setw(4) << setfill('0') << num;
    return ss.str();
}

// テーブルの1行(開始点と終着点のペア)
struct RainbowRow
{
    string start;
    string end;
};

// テーブルの事前生成
vector<RainbowRow> generate_table()
{
    vector<RainbowRow> table;
    for (int i = 0; i < TABLE_SIZE; ++i)
    {
        // 開始点がバラけるように等間隔で初期パスワードを生成
        int start_num = (i * (PASSWORD_SPACE / TABLE_SIZE)) % PASSWORD_SPACE;
        stringstream ss;
        ss << setw(4) << setfill('0') << start_num;
        string start_p = ss.str();
        string current_p = start_p;
        // チェインを最後まで伸ばす
        for (int step = 0; step < CHAIN_LEN; ++step)
        {
            string h = md5(current_p);
            current_p = reduce(h, step);
        }
        // 開始点と最終的な縮約結果を保存
        table.push_back({start_p, current_p});
    }
    return table;
}

// レインボーテーブルからの探索
string search_table(const string &target_hash, const vector<RainbowRow> &table)
{
    // ターゲットハッシュがチェインの「どの位置」にあるかを後ろから逆算していく
    for (int k = CHAIN_LEN - 1; k >= 0; --k)
    {
        string current_hash = target_hash;
        string current_p = "";
        // k番目のステップから最後のステップまでシミュレート
        for (int step = k; step < CHAIN_LEN; ++step)
        {
            current_p = reduce(current_hash, step);
            if (step < CHAIN_LEN - 1)
            {
                current_hash = md5(current_p);
            }
        }
        // シミュレートした末尾(current_p)がテーブルのendに存在するかチェック
        for (const auto &row : table)
        {
            if (row.end == current_p)
            {
                // ヒットしたら、その行の開始点(start)からチェインを再現して検証
                string recon_p = row.start;
                for (int step = 0; step < CHAIN_LEN; ++step)
                {
                    string recon_h = md5(recon_p);
                    if (recon_h == target_hash)
                    {
                        return recon_p; // パスワード復元成功
                    }
                    recon_p = reduce(recon_h, step);
                }
            }
        }
    }
    return ""; // テーブルのカバー範囲外で見つからなかった場合
}

int main()
{
    // g++ -O3 rainbow-attack.cpp -o rainbow-attack.out -lcrypto && ./rainbow-attack.out
    auto table = generate_table();
    string target_hash;
    cout << "Enter the target hash: ";
    cin >> target_hash;
    string result = search_table(target_hash, table);
    if (result.empty())
    {
        cout << "Password not found in the table." << endl;
    }
    else
    {
        cout << "Password found: " << result << endl;
    }
    return 0;
}