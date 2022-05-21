// Задание 1
// Реализовать класс, описывающий окружность. В классе долж-
// ны быть следующие компоненты:
// ■ поле, хранящее радиус окружности;
// ■ get-свойство, возвращающее радиус окружности;
// ■ set-свойство, устанавливающее радиус окружности;
// ■ get-свойство, возвращающее диаметр окружности;
// ■ метод, вычисляющий площадь окружности;
// ■ метод, вычисляющий длину окружности.
// Продемонстрировать работу свойств и методов.


class Circle {
    radius = 0;

    get radius() {
        return this.radius;
    }

    set set_radius(r) {
        this.radius = r;
    }
    get diametr() {
        return this.radius ** 2;
    }

    CircleArea() {
        return Math.floor(Math.PI * this.diametr * 100) / 100;
    }

    CircleWidth() {
        return Math.floor(2 * Math.PI * this.radius * 100) / 100;
    }

}

var circle = new Circle();
circle.set_radius = 6;

document.write("Radius=" + circle.radius + "<br>Diameter=" + circle.diametr + "<br>Circle round=" + circle.CircleArea() + "<br>Circle width=" + circle.CircleWidth());

// Задание 2
// Реализовать класс, описывающий html элемент.
// Класс HtmlElement должен содержать внутри себя:
// ■ название тега;
// ■ самозакрывающийся тег или нет;
// ■ текстовое содержимое;
// ■ массив атрибутов;
// ■ массив стилей;
// ■ массив вложенных таких же тегов;
// ■ метод для установки атрибута;
// ■ метод для установки стиля;
// ■ метод для добавления вложенного элемента в конец теку-
// щего элемента;
// ■ метод для добавления вложенного элемента в начало те-
// кущего элемента;
// ■ метод getHtml(), который возвращает html код в виде
// строки, включая html код вложенных элементов.
// С помощью написанного класса реализовать следующий блок
// и добавить его на страницу с помощью document.write().
document.write("<br><br>");

class HtmlElement {
    tag_Name = '';
    isSelfClothing = false;
    text_inside = '';
    atributes = [];
    styles = [];
    nested_tags = [];
    constructor(tagName, isSelfClosing, text) {
        this.tag_Name = tagName;
        this.isSelfClothing = isSelfClosing;
        this.text_inside = text;
    }
    atribut_Push(atr) {
        return this.atributes.push(atr);
    }
    style_Push(style) {
        return this.styles.push(style);
    }
    appendTag(tag) {
        return this.nested_tags.push(tag.html);
    }
    prependTag(tag) {
        return this.nested_tags.unshift(tag.html);
    }
    get html() {
        let html = '';
        if (this.isSelfClothing === false) {
            html = `<${this.tag_Name} ${this.atributes.join('')} style="${this.styles.join('')}">${this.text_inside}${this.nested_tags.join(' ')}</${this.tag_Name}>`;
        } else {
            html = `<${this.tag_Name} ${this.atributes.join('')} style="${this.styles.join('')}">${this.text_inside}${this.nested_tags.join(' ')}`;
        }
        return html;
    }
}

const atributes = [
    {
        name: 'id="wrapper"',
    },
    {
        name: 'src="./Lorem.png"',
    },
    {
        name: 'alt="Lorem Ipsum"',
    },
    {
        name: 'href="http://www.lipsum.com/"',
    },
    {
        name: 'target="_blank"',
    },
];

const styles = [
    {
        name: 'display:flex;',
    },
    {
        name: 'width:300px;',
    },
    {
        name: 'width:100%;',
    },
    {
        name: 'text-align:justify;',
    },
    {
        name: 'margin: 10px;',
    },
];

const wrapper = new HtmlElement('div', false, '');
wrapper.atribut_Push(atributes[0].name);
wrapper.style_Push(styles[0].name);

const div = new HtmlElement('div', false, '');
div.style_Push(styles[1].name);
div.style_Push(styles[4].name);

const h3 = new HtmlElement('h3', false, 'What is lorem Ipsum?');

const img = new HtmlElement('img', true, '');
img.style_Push(styles[2].name);
img.atribut_Push(atributes[1].name);
img.atribut_Push(atributes[2].name);

const p = new HtmlElement(
    'p',
    false,
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat quia nobis corporis, maiores esse rerum error laboriosam voluptatibus nihil, veritatis quisquam beatae repudiandae illum porro nemo neque consequuntur quis illo natus qui dolores voluptates, tempora ad. Pariatur quisquam distinctio maxime. Tenetur, expedita id. Provident ut sit blanditiis eveniet ipsam voluptatum?'
);
p.style_Push(styles[3].name);

const a = new HtmlElement('a', false, 'More...');
a.atribut_Push(atributes[3].name + ' ');
a.atribut_Push(atributes[4].name);

div.prependTag(p);
div.prependTag(img);
div.prependTag(h3);
div.appendTag(a);
wrapper.prependTag(div);
wrapper.appendTag(div);

document.write(wrapper.html);
document.write("<br><br>");

// Задание 3
// Реализовать класс, который описывает css класс.
// Класс CssClass должен содержать внутри себя:
// ■ название css класса;
// ■ массив стилей;
// ■ метод для установки стиля;
// ■ метод для удаления стиля;
// ■ метод getCss(), который возвращает css код в виде строки.

class CssClass {
    class_name = '';
    styles = [];
    constructor(name = null, styles = []) {
        this.class_name = name;
        this.styles = styles;
    }
    setStyle(style) {
        if (this.styles == null) {
            this.styles = [style]
        }
        else {
            this.styles.push(style)
        }
    }
    deleteStyle(style) {
        if (this.styles != null && this.styles.includes(style)) {
            this.styles = this.styles.filter(i => i !== style)
        }
    }
    getCss() {
        return `${this.class_name} {\n\t${this.styles != null ? `${this.styles.join(';\n\t')};` : ``}\n}`
    }
}

let class1 = new CssClass('.class1')
class1.setStyle('display: flex')

let class2 = new CssClass('.class2')
class2.setStyle('width: 300px')
class2.setStyle('margin: 10px')

let class3 = new CssClass('.class3')
class3.setStyle('width: 100px')
class3.setStyle('height: 100px')

let classText = new CssClass('.text')
classText.setStyle('text-align: justify')

let classImg = new CssClass('img')
classImg.setStyle('width: 300px')
classImg.setStyle('height: 300px')

console.log(class1, class2, class3, classText, classImg);
console.log(classImg.getCss());


// Задание 4
// Реализовать класс, описывающий блок html документ.
// Класс HtmlBlock должен содержать внутри себя:
// ■ коллекцию стилей, описанных с помощью класса CssClass;
// ■ корневой элемент, описанный с помощью класса
// HtmlElement;
// ■ метод getCode(), который возвращает строку с html ко-
// дом (сначала теги style с описанием всех классов, а потом
// все html содержимое из корневого тега и его вложенных
// элементов).
// С помощью написанных классов реализовать следующий блок
// (см. рис. 2) и добавить его на страницу с помощью document.write().

class HtmlBlock {
    _styles = [];
    _root = null;

    constructor(styles = [], root = null) {
        this._styles = styles
        this._root = root
    }
    getCode() {
        return `<style>\n${this._styles.flatMap(s => s.getCss()).join('\n')}\n</style>\n${this._root.html}`
    }
}


let clsWrap = new CssClass('.wrap')
clsWrap.setStyle('display: flex')

let clsBlock = new CssClass('.block')
clsBlock.setStyle('width: 300px')
clsBlock.setStyle('margin: 10px')

let clsImg = new CssClass('.img')
clsImg.setStyle('width: 100%')

let clsText = new CssClass('.text')
clsText.setStyle('text-align: justify')



htmlB = new HtmlBlock([clsWrap, clsBlock, clsImg, clsText], wrapper)

console.log(htmlB.getCode());
document.write(htmlB.getCode())