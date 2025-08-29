// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
unsigned int dict_size = 0;

// Returns true if word is in dictionary, else false
// 对哈希表中的链表进行搜索，如果匹配返回true
bool check(const char *word)
{
    // TODO
    unsigned int index = hash(word);
    for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
// 对单词开头取索引数，如果大于26则对N取余
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int index = toupper(word[0]) - 'A';
    if (index >= N)
    {
        index %= N;
    }
    return index;
}

// Loads ` into memory, returning true if successful, else false
// 将字典加载到内存并统计单词个数

bool load(const char *dictionary)
{
    // 打开字典
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    // 读取字典单词
    char word[LENGTH + 1];
    while (fscanf(source, "%s", word) != EOF)
    {
        unsigned int num = hash(word);
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        strcpy(new_node->word, word);
        new_node->next = table[num];
        table[num] = new_node;
        dict_size++;
    }

    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
// 循环释放table表中的所有内存

bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *n = table[i];
        while (n != NULL)
        {
            node *tmp = n;
            n = n->next;
            free(tmp);
        }
        if (i == N - 1 && n == NULL)
        {
            return true;
        }
    }
    return false;
}
