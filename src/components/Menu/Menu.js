import { Link } from "react-router-dom";

const Menu = (props) => {
  return (
    <nav>
      <ul>
        <Link to="/">
          <li>Home</li>
        </Link>
        <Link to="/key">
          <li>Clave dicotómica</li>
        </Link>
        <Link to="/form">
          <li>Formulario</li>
        </Link>
      </ul>
    </nav>
  );
};

export default Menu;
