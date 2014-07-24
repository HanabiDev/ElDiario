/**
 * Adobe Edge: symbol definitions
 */
(function($, Edge, compId){
//images folder
var im='/media/uploads/ads/pos1/images/';

var fonts = {};
var opts = {};
var resources = [
];
var symbols = {
"stage": {
    version: "3.0.0",
    minimumCompatibleVersion: "3.0.0",
    build: "3.0.0.322",
    baseState: "Base State",
    scaleToFit: "none",
    centerStage: "none",
    initialState: "Base State",
    gpuAccelerate: false,
    resizeInstances: false,
    content: {
            dom: [
            {
                id: 'diario',
                type: 'image',
                rect: ['0px', '191px','143px','120px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"734113_389386964485689_331498768_n.jpg",'0px','0px']
            },
            {
                id: 'Text',
                type: 'text',
                rect: ['143px', '192px','auto','auto','auto', 'auto'],
                text: "Paute aqui",
                font: ['Arial, Helvetica, sans-serif', 104, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'g3721',
                type: 'image',
                rect: ['558px', '0px','487px','120px','auto', 'auto'],
                opacity: 0,
                fill: ["rgba(0,0,0,0)",im+"g3721.png",'0px','0px']
            }],
            symbolInstances: [

            ]
        },
    states: {
        "Base State": {
            "${_Stage}": [
                ["color", "background-color", 'rgba(255,255,255,0.00)'],
                ["style", "width", '1038px'],
                ["style", "height", '120px'],
                ["style", "overflow", 'hidden']
            ],
            "${_diario}": [
                ["style", "top", '191px'],
                ["style", "height", '120px'],
                ["style", "left", '0px'],
                ["style", "width", '143px']
            ],
            "${_Text}": [
                ["style", "top", '192px'],
                ["style", "left", '143px'],
                ["style", "font-size", '104px']
            ],
            "${_g3721}": [
                ["style", "top", '0px'],
                ["style", "height", '120px'],
                ["style", "opacity", '0'],
                ["style", "left", '558px'],
                ["style", "width", '487px']
            ]
        }
    },
    timelines: {
        "Default Timeline": {
            fromState: "Base State",
            toState: "",
            duration: 6000,
            autoPlay: true,
            timeline: [
                { id: "eid13", tween: [ "style", "${_diario}", "top", '0px', { fromValue: '191px'}], position: 0, duration: 3000 },
                { id: "eid15", tween: [ "style", "${_g3721}", "opacity", '1', { fromValue: '0'}], position: 3000, duration: 1000 },
                { id: "eid14", tween: [ "style", "${_Text}", "top", '0px', { fromValue: '192px'}], position: 0, duration: 3000 }            ]
        }
    }
}
};


Edge.registerCompositionDefn(compId, symbols, fonts, resources, opts);

/**
 * Adobe Edge DOM Ready Event Handler
 */
$(window).ready(function() {
     Edge.launchComposition(compId);
});
})(jQuery, AdobeEdge, "banner");
