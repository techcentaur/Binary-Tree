#include <iostream>

using namespace std;

class Node;

template <class K, class V>
class Binarytree{

    Node rootnode = Node(K(), V());

    class Node{
    public:
        K key;
        V value;
        Node left = Binarytree::Node(K(), V());
        Node right = Binarytree::Node(K(), V());
        Node parent = Binarytree::Node(K(), V());

        Node(K key, V value){
            this->key=key;
            this->value=value;
            this->left = nullptr;
            this->right = nullptr;
            this->parent = nullptr;
        }
    };

    Binarytree(K key, V value){
        this->rootnode = Node(key, value);
    }

    void insert(K key, V value){
        _insert(rootnode, key, value);
    }
    void _insert(Node root, K key, V value){
        if (root.key>key){
            if (root.left){

            }

        } else if (root.key < key){

        } else{
            cout<<"[?][?] Key already exists...!";
        }

    }
};


int main() {
    cout << "Hello, World!" << endl;
    return 0;
}