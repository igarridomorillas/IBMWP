import Menu from "./Menu/Menu";

const Header = (props) => {
  return (
    <header className="container">
      <h1 className="header__title">IBMWP</h1>
      <Menu />
    </header>
  );
};

export default Header;
