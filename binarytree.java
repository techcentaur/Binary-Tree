public class Binarytree<Key extends Comparable<Key>, Value>
{

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

    Binarytree{

    }


}
