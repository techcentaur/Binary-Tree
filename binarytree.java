import java.lang.*;

public class Binarytree<Key extends Comparable<Key>, Value>
{
    private Node root;

    private class Node {
        Key key;
        Value val;
        Node leftT;
        Node rightT;
        Node parent;

        Node (Key key, Value val){
            this.key = key;
            this.val = val;
        }
    }

    Binarytree(Key key, Value val){
        this.root = new Node(key, val);
    }

    private boolean isLeaf(Node n){
        return (n.leftT != null) && (n.rightT != null);
    }

    public void insert(Key key, Value val){
        _insert(key, val, root);
    }
    private void _insert(Key key, Value val, Node rootNode){
        if (rootNode.key == key) System.out.println("[?][?] Key already exists!");

        if ((rootNode.key).compareTo(key) > 0){
            if (rootNode.leftT != null) _insert(key, val, rootNode.leftT);
            else {
                Node n = new Node(key, val);
                rootNode.leftT = n;
                n.parent = rootNode;
            }
        }
        else if((rootNode.key).compareTo(key) < 0){
            if( rootNode.rightT != null) _insert(key, val, rootNode.rightT);
            else {
                Node n = new Node(key, val);
                rootNode.rightT = n;
                n.parent = rootNode;
            }
        }
    }

    public boolean search(Key key){
        return _search(key, root);
    }
    private boolean _search(Key key, Node rootNode){
        boolean b = false;
        if (rootNode.key.compareTo(key) == 0) {
                System.out.println("[*][*] Key successfully found!");
                return b = true;
            }
            else if (rootNode.key.compareTo(key) > 0){
                b = _search(key, rootNode.leftT);

            }
            else if (rootNode.key.compareTo(key) < 0) {
                b = _search(key, rootNode.rightT);
        }
        return b;
    }

    int main(){
        Binarytree<Key, Value> b = new Binarytree<Key,Value>(5, 5);
    }
}
