import org.chocosolver.solver.Model;
import org.chocosolver.solver.variables.IntVar;

public class TestChoco {
    public static void main(String[] args) {
        Model model = new Model("simple");
        IntVar x = model.intVar("X", 0, 5);
        IntVar y = model.intVar("Y", 0, 5);

        model.arithm(x, "+", y, "=", 5).post();

        if (model.getSolver().solve()) {
            System.out.println("X=" + x.getValue() + " Y=" + y.getValue());
        }
    }
}