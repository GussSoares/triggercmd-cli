(function(t){function e(e){for(var r,n,s=e[0],l=e[1],c=e[2],u=0,d=[];u<s.length;u++)n=s[u],Object.prototype.hasOwnProperty.call(a,n)&&a[n]&&d.push(a[n][0]),a[n]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(t[r]=l[r]);m&&m(e);while(d.length)d.shift()();return i.push.apply(i,c||[]),o()}function o(){for(var t,e=0;e<i.length;e++){for(var o=i[e],r=!0,n=1;n<o.length;n++){var s=o[n];0!==a[s]&&(r=!1)}r&&(i.splice(e--,1),t=l(l.s=o[0]))}return t}var r={},n={app:0},a={app:0},i=[];function s(t){return l.p+"js/"+({about:"about",home:"home"}[t]||t)+"."+{about:"2fb24c4d",home:"5c5b7a7c"}[t]+".js"}function l(e){if(r[e])return r[e].exports;var o=r[e]={i:e,l:!1,exports:{}};return t[e].call(o.exports,o,o.exports,l),o.l=!0,o.exports}l.e=function(t){var e=[],o={about:1,home:1};n[t]?e.push(n[t]):0!==n[t]&&o[t]&&e.push(n[t]=new Promise((function(e,o){for(var r="css/"+({about:"about",home:"home"}[t]||t)+"."+{about:"235467fe",home:"a3d2485f"}[t]+".css",a=l.p+r,i=document.getElementsByTagName("link"),s=0;s<i.length;s++){var c=i[s],u=c.getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(u===r||u===a))return e()}var d=document.getElementsByTagName("style");for(s=0;s<d.length;s++){c=d[s],u=c.getAttribute("data-href");if(u===r||u===a)return e()}var m=document.createElement("link");m.rel="stylesheet",m.type="text/css",m.onload=e,m.onerror=function(e){var r=e&&e.target&&e.target.src||a,i=new Error("Loading CSS chunk "+t+" failed.\n("+r+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=r,delete n[t],m.parentNode.removeChild(m),o(i)},m.href=a;var f=document.getElementsByTagName("head")[0];f.appendChild(m)})).then((function(){n[t]=0})));var r=a[t];if(0!==r)if(r)e.push(r[2]);else{var i=new Promise((function(e,o){r=a[t]=[e,o]}));e.push(r[2]=i);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,l.nc&&u.setAttribute("nonce",l.nc),u.src=s(t);var d=new Error;c=function(e){u.onerror=u.onload=null,clearTimeout(m);var o=a[t];if(0!==o){if(o){var r=e&&("load"===e.type?"missing":e.type),n=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+r+": "+n+")",d.name="ChunkLoadError",d.type=r,d.request=n,o[1](d)}a[t]=void 0}};var m=setTimeout((function(){c({type:"timeout",target:u})}),12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(e)},l.m=t,l.c=r,l.d=function(t,e,o){l.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},l.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},l.t=function(t,e){if(1&e&&(t=l(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(l.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)l.d(o,r,function(e){return t[e]}.bind(null,r));return o},l.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return l.d(e,"a",e),e},l.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},l.p="/",l.oe=function(t){throw console.error(t),t};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],u=c.push.bind(c);c.push=e,c=c.slice();for(var d=0;d<c.length;d++)e(c[d]);var m=u;i.push([0,"chunk-vendors"]),o()})({0:function(t,e,o){t.exports=o("56d7")},"034f":function(t,e,o){"use strict";o("85ec")},"3f7a":function(t,e,o){"use strict";var r=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-dialog",{attrs:{"max-width":"290"},model:{value:t.show,callback:function(e){t.show=e},expression:"show"}},[o("v-card",[t.edit?o("v-card-title",{staticClass:"text-h5"},[t._v(" "+t._s(t.dialogTitle)+": "),o("i",[t._v(t._s(t.title))])]):o("v-card-title",{staticClass:"text-h5"},[t._v(" "+t._s(t.dialogTitle)+" ")]),o("v-card-text",[o("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[o("v-row",[o("v-col",{attrs:{cols:""}},[o("v-text-field",{attrs:{label:"Trigger","hide-details":"auto",rules:t.rules},model:{value:t.form.trigger,callback:function(e){t.$set(t.form,"trigger",e)},expression:"form.trigger"}})],1)],1),o("v-row",[o("v-col",{attrs:{cols:""}},[o("v-text-field",{attrs:{label:"Command","hide-details":"auto",rules:t.rules},model:{value:t.form.command,callback:function(e){t.$set(t.form,"command",e)},expression:"form.command"}})],1)],1),o("v-row",[o("v-col",{attrs:{cols:""}},[o("v-select",{attrs:{label:"Ground","hide-details":"auto",items:["foreground","background"],rules:t.rules},model:{value:t.form.ground,callback:function(e){t.$set(t.form,"ground",e)},expression:"form.ground"}})],1)],1),o("v-row",[o("v-col",{attrs:{cols:""}},[o("v-switch",{attrs:{label:"Allow Params: "+t.form.allowParams},model:{value:t.form.allowParams,callback:function(e){t.$set(t.form,"allowParams",e)},expression:"form.allowParams"}})],1)],1),o("v-row",[o("v-col",{attrs:{cols:""}},[o("v-text-field",{attrs:{label:"Voice","hide-details":"auto",rules:t.rules},model:{value:t.form.voice,callback:function(e){t.$set(t.form,"voice",e)},expression:"form.voice"}})],1)],1)],1)],1),o("v-card-actions",[o("v-spacer"),o("v-btn",{attrs:{color:"green darken-1",text:""},on:{click:function(e){return t.confirm()}}},[t._v(" Save ")]),o("v-btn",{attrs:{color:"red darken-1",text:""},on:{click:function(e){t.show=!1}}},[t._v(" Cancel ")])],1)],1)],1)},n=[],a=(o("d3b7"),o("25f0"),{props:{edit:Boolean,dialogTitle:String,value:Boolean,trigger:String,command:String,ground:String,allowParams:Boolean,voice:String,confirmFunction:Function},data:function(){return{title:this.trigger,valid:!0,form:{trigger:this.trigger,command:this.command,ground:this.ground,allowParams:this.allowParams,voice:this.voice},rules:[function(t){return!!t||"Input is required"}]}},computed:{show:{get:function(){return this.value},set:function(t){this.$refs.form.resetValidation(),this.$emit("input",t)}}},methods:{confirm:function(){this.$refs.form.validate()&&(this.edit?this.editCommand():this.createCommand())},editCommand:function(){var t=this;return this.$http.patch("/command?old_title=".concat(this.trigger),{trigger:this.form.trigger,command:this.form.command,ground:this.form.ground,allowParams:this.form.allowParams.toString(),voice:this.form.voice}).then((function(e){t.show=!1,t.$root.$emit("reload",{}),t.$root.$emit("snackbar",{color:"success",message:'"'.concat(t.form.trigger,'" edited successfuly!')})})).catch((function(e){t.show=!1,t.$root.$emit("snackbar",{color:"error",message:e.toString()})}))},createCommand:function(){var t=this;return this.$http.post("/command",{trigger:this.form.trigger,command:this.form.command,ground:this.form.ground,allowParams:this.form.allowParams.toString(),voice:this.form.voice}).then((function(e){t.show=!1,t.$root.$emit("reload",{}),t.$root.$emit("snackbar",{color:"success",message:'"'.concat(t.form.trigger,'" created successfuly!')}),t.$refs.form.reset()})).catch((function(e){t.show=!1,t.$root.$emit("snackbar",{color:"error",message:e.toString()})}))}}}),i=a,s=o("2877"),l=o("6544"),c=o.n(l),u=o("8336"),d=o("b0af"),m=o("99d9"),f=o("62ad"),v=o("169a"),h=o("4bd4"),p=o("0fd9"),g=o("b974"),b=o("2fa4"),w=o("b73d"),k=o("8654"),_=Object(s["a"])(i,r,n,!1,null,null,null);e["a"]=_.exports;c()(_,{VBtn:u["a"],VCard:d["a"],VCardActions:m["a"],VCardText:m["b"],VCardTitle:m["c"],VCol:f["a"],VDialog:v["a"],VForm:h["a"],VRow:p["a"],VSelect:g["a"],VSpacer:b["a"],VSwitch:w["a"],VTextField:k["a"]})},"56d7":function(t,e,o){"use strict";o.r(e);o("e260"),o("e6cf"),o("cca6"),o("a79d");var r=o("2b0e"),n=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-app",["Login"!==this.$router.currentRoute.name?o("appbar",{model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}}):t._e(),"Login"!==this.$router.currentRoute.name?o("drawer",{model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}}):t._e(),o("v-main",[o("v-container",{attrs:{fluid:""}},[o("router-view"),"Login"!==this.$router.currentRoute.name?o("v-btn",{directives:[{name:"show",rawName:"v-show",value:!t.hidden,expression:"!hidden"}],attrs:{color:"pink",dark:"",fixed:"",bottom:"",right:"",fab:"",elevation:"24"},on:{click:function(e){t.showModal=!0}}},[o("v-icon",[t._v("mdi-plus")])],1):t._e()],1)],1),o("Dialog",{attrs:{dialogTitle:"New Command",trigger:t.form.trigger,command:t.form.command,ground:t.form.ground,allowParams:t.form.allowParams,voice:t.form.voice},model:{value:t.showModal,callback:function(e){t.showModal=e},expression:"showModal"}})],1)},a=[],i=(o("b0c0"),function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("v-navigation-drawer",{attrs:{app:""},model:{value:t.show,callback:function(e){t.show=e},expression:"show"}},[o("v-list",[o("v-list-item",{staticClass:"px-2"},[o("v-list-item-avatar",[o("v-img",{attrs:{src:"https://s.gravatar.com/avatar/61b772d41966203ba1784dd9469f050b?s=80"}})],1)],1),o("v-list-item",{attrs:{link:""}},[o("v-list-item-content",[o("v-list-item-title",{staticClass:"text-h6"},[t._v(" Gustavo Soares ")]),o("v-list-item-subtitle",[t._v("gustavo.soares.cdc@gmail.com")])],1)],1)],1),o("v-divider"),o("v-list",{attrs:{nav:"",dense:""}},[o("v-list-item",{attrs:{link:""}},[o("v-list-item-icon",[o("v-icon",[t._v("mdi-monitor")])],1),o("v-list-item-title",[t._v("Computers")])],1),o("v-list-item",{attrs:{link:""}},[o("v-list-item-icon",[o("v-icon",[t._v("mdi-view-dashboard")])],1),o("v-list-item-title",[t._v("Commands")])],1)],1)],1)],1)}),s=[],l={props:{value:Boolean},data:function(){return{}},methods:{},computed:{show:{get:function(){return this.value},set:function(t){this.$emit("input",t)}}}},c=l,u=o("2877"),d=o("6544"),m=o.n(d),f=o("ce7e"),v=o("132d"),h=o("adda"),p=o("8860"),g=o("da13"),b=o("8270"),w=o("5d23"),k=o("34c3"),_=o("f774"),x=Object(u["a"])(c,i,s,!1,null,null,null),V=x.exports;m()(x,{VDivider:f["a"],VIcon:v["a"],VImg:h["a"],VList:p["a"],VListItem:g["a"],VListItemAvatar:b["a"],VListItemContent:w["a"],VListItemIcon:k["a"],VListItemSubtitle:w["b"],VListItemTitle:w["c"],VNavigationDrawer:_["a"]});var y=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-app-bar",{attrs:{app:"",color:"#006784",dark:""}},[o("v-app-bar-nav-icon",{on:{click:function(e){e.stopPropagation(),t.showDrawer=!t.showDrawer}}}),o("div",{staticClass:"d-flex align-center"},[o("v-img",{staticClass:"shrink mt-1",attrs:{alt:"Vuetify Name",contain:"","min-width":"100",src:"https://www.triggercmd.com/user/images/logoColor.png",width:"200"}})],1),o("v-spacer")],1)},$=[],C={props:{value:Boolean},data:function(){return{}},computed:{showDrawer:{get:function(){return this.value},set:function(t){this.$emit("input",t)}}}},P=C,S=o("40dc"),A=o("5bc1"),L=o("2fa4"),O=Object(u["a"])(P,y,$,!1,null,null,null),j=O.exports;m()(O,{VAppBar:S["a"],VAppBarNavIcon:A["a"],VImg:h["a"],VSpacer:L["a"]});var E=o("3f7a"),T={name:"App",components:{Drawer:V,Appbar:j,Dialog:E["a"]},data:function(){return{hidden:!1,showModal:!1,drawer:!1,form:{trigger:null,command:null,ground:null,allowParams:!1,voice:null}}},created:function(){console.log(this.$router.currentRoute.name),console.log(Object({NODE_ENV:"production",VUE_APP_API_URL:"http://localhost:9075",BASE_URL:"/"}))}},N=T,I=(o("034f"),o("7496")),B=o("8336"),D=o("a523"),M=o("f6c4"),F=Object(u["a"])(N,n,a,!1,null,null,null),R=F.exports;m()(F,{VApp:I["a"],VBtn:B["a"],VContainer:D["a"],VIcon:v["a"],VMain:M["a"]});var U=o("9483");Object(U["a"])("".concat("/","service-worker.js"),{ready:function(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/AFskqB")},registered:function(){console.log("Service worker has been registered.")},cached:function(){console.log("Content has been cached for offline use.")},updatefound:function(){console.log("New content is downloading.")},updated:function(){console.log("New content is available; please refresh.")},offline:function(){console.log("No internet connection found. App is running in offline mode.")},error:function(t){console.error("Error during service worker registration:",t)}});o("d3b7"),o("3ca3"),o("ddb0");var q=o("8c4f");r["a"].use(q["a"]);var G=[{path:"/",component:function(){return o.e("home").then(o.bind(null,"bb51"))},auth:!0,children:[{path:"",name:"Home",component:function(){return o.e("home").then(o.bind(null,"bb51"))}},{path:"about",name:"About",component:function(){return o.e("about").then(o.bind(null,"f820"))}}]},{path:"/login",name:"Login",component:function(){return o.e("about").then(o.bind(null,"a55b"))}},{path:"*",name:"NotFound",component:function(){return o.e("about").then(o.bind(null,"9703"))}}],H=new q["a"]({mode:"history",base:"/",routes:G}),J=H,z=o("2f62");r["a"].use(z["a"]);var K=new z["a"].Store({state:{},mutations:{},actions:{},modules:{}}),Q=o("f309");r["a"].use(Q["a"]);var W=new Q["a"]({}),X=o("bc3a"),Y=o.n(X);r["a"].config.productionTip=!1,r["a"].prototype.$http=Y.a.create({baseURL:"http://localhost:9075"}),new r["a"]({router:J,store:K,vuetify:W,render:function(t){return t(R)}}).$mount("#app")},"85ec":function(t,e,o){}});
//# sourceMappingURL=app.0349c2ec.js.map