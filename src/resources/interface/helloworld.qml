Item {
    Column {
        id: column1
        x: 0
        y: 0
        width: 260
        height: 480

        Image {
            id: image1
            width: 243
            height: 458
            antialiasing: true
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 22
            anchors.left: parent.left
            anchors.leftMargin: 0
            anchors.right: parent.right
            anchors.rightMargin: 17
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            fillMode: Image.Tile
            source: "qrc:/qtquickplugin/images/template_image.png"
        }
    }

    Flickable {
        id: flickable1
        x: 292
        y: 111
        width: 300
        height: 300

        PathView {
            id: pathView1
            x: -5
            y: 60
            width: 250
            height: 130
            model: ListModel {
                ListElement {
                    name: "Grey"
                    colorCode: "grey"
                }

                ListElement {
                    name: "Red"
                    colorCode: "red"
                }

                ListElement {
                    name: "Blue"
                    colorCode: "blue"
                }

                ListElement {
                    name: "Green"
                    colorCode: "green"
                }
            }
            delegate: Component {
                Column {
                    Rectangle {
                        width: 40
                        height: 40
                        color: colorCode
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    Text {
                        x: 5
                        text: name
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.bold: true
                    }
                    spacing: 5
                }
            }
            path: Path {
                startY: 100
                startX: 120
                PathQuad {
                    x: 120
                    y: 25
                    controlY: 75
                    controlX: 260
                }

                PathQuad {
                    x: 120
                    y: 100
                    controlY: 75
                    controlX: -20
                }
            }
        }
    }

}
