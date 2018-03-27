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

    public Binarytree(Key key, Value val){
        this.root = new Node(key, val);
    }

    private boolean isLeaf(Node n){
        return (n.leftT == null) && (n.rightT == null);
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
                System.out.println("[*][*] Key successfully found! ");
                return b = true;
            }
            else if (rootNode.key.compareTo(key) > 0){
                if (rootNode.leftT != null) {
                    b = _search(key, rootNode.leftT);
                }
                else{
                    System.out.println("[?][?] Key doesn't exist! ");
                }
            }
            else if (rootNode.key.compareTo(key) < 0) {
                if(rootNode.rightT!=null){
                    b = _search(key, rootNode.rightT);
                }
                else System.out.println("[?][?] Key doesn't exist! ");
        }
        return b;
    }

    public void display(){
        System.out.print("[*] Displaying Tree : ");
        _display(root);
        System.out.println("");
    }
    private void _display(Node rootNode){
        if(rootNode.leftT!=null){
            System.out.print("[");
            _display(rootNode.leftT);
            System.out.print("]");
        }

        System.out.print(rootNode.val);

        if(rootNode.rightT!=null){
            System.out.print("[");
            _display(rootNode.rightT);
            System.out.print("]");
        }
    }

    private void delete(Key key){
        _delete(key, root);
    }
    private void _delete(Key key, Node rootNode){
        if (rootNode.key.equals(key)){
            if (isLeaf(rootNode)){
                if (rootNode==root) root.key=null;
                else{
                    if (rootNode.parent.leftT==rootNode) rootNode.parent.leftT=null;
                    else rootNode.parent.rightT=null;
                }
            } else if (rootNode.leftT==null){
                if(rootNode.rightT.key.compareTo(rootNode.parent.key) > 0){
                    rootNode.parent.rightT = rootNode.rightT;
                    rootNode.rightT.parent = rootNode.parent;
                } else{
                    rootNode.parent.leftT = rootNode.rightT;
                    rootNode.rightT.parent = rootNode.parent;
                }
            } else if(rootNode.rightT==null){
                if (rootNode.leftT.key.compareTo(rootNode.parent.key) > 0){
                    rootNode.parent.rightT = rootNode.leftT;
                    rootNode.leftT.parent = rootNode.parent;
                } else{
                    rootNode.parent.leftT = rootNode.leftT;
                    rootNode.leftT.parent = rootNode.parent;
                }
            } else{
                Node n = predecessor(rootNode.leftT);
                delete(n.key);
                rootNode.key = n.key;
            }
        }
        else if((rootNode.key.compareTo(key)) > 0) _delete(key, rootNode.leftT);
        else if((rootNode.key.compareTo(key)) < 0) _delete(key, rootNode.rightT);
        else System.out.print("[?][?] Key doesn't exist...!");

    }

    private Node predecessor(Node rootNode){
        Node n1;
        if(rootNode.rightT==null) return rootNode;
        else n1 = predecessor(rootNode.rightT);
        return n1;
    }

    public static void main(String[] args){
        Binarytree<Integer, Integer> b = new Binarytree<>(5, 5);
        b.insert(1,1);
        b.insert(10, 10);
        b.insert(2, 2);
        b.insert(4, 4);
        b.insert(7, 7);
        b.insert(18, 18);
        b.insert(0, 0);
        b.insert(14, 14);
        b.insert(6, 6);
        b.insert(3, 3);
        b.display() ;
        b.delete(5);
        b.display();
    }
}