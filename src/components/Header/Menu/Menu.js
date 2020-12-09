import { Link } from "react-router-dom";
import * as ReactBootstrap from "react-bootstrap";

const Menu = (props) => {
  return (
    <>
      {/* <nav className="container">
        <ul className="row row-cols-auto g-2">
          <Link to="/" className="col">
            <li className="p-3 border bg-light">Inicio</li>
          </Link>
          <Link to="/key" className="col">
            <li className="p-3 border bg-light">Clave dicotómica</li>
          </Link>
          <Link to="/form" className="col">
            <li className="p-3 border bg-light">Formulario</li>
          </Link>
        </ul>
      </nav> */}
      <ReactBootstrap.Navbar
        collapseOnSelect
        expand="lg"
        bg="secondary"
        variant="dark"
      >
        <ReactBootstrap.Navbar.Brand href="/" className="px-3">
          Inicio
        </ReactBootstrap.Navbar.Brand>
        <ReactBootstrap.Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <ReactBootstrap.Navbar.Collapse id="responsive-navbar-nav">
          <ReactBootstrap.Nav className="ml-auto px-3">
            <ReactBootstrap.Nav.Link href="#/key" className="text-light">
              Clave dicotómica
            </ReactBootstrap.Nav.Link>
            <ReactBootstrap.Nav.Link href="#/form" className="text-light">
              Calcular índice
            </ReactBootstrap.Nav.Link>
          </ReactBootstrap.Nav>
          {/* <ReactBootstrap.Nav>
            <ReactBootstrap.Nav.Link href="">
              More deets
            </ReactBootstrap.Nav.Link>
            <ReactBootstrap.Nav.Link eventKey={2} href="">
              Dank memes
            </ReactBootstrap.Nav.Link>
          </ReactBootstrap.Nav> */}
        </ReactBootstrap.Navbar.Collapse>
      </ReactBootstrap.Navbar>
    </>
  );
};

export default Menu;
