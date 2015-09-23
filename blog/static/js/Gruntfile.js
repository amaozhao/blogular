module.exports = function(grunt){

    // 项目配置
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                mangle: false,
                preserveComments: false, //不删除注释，还可以为 false（删除全部注释），some（保留@preserve @license @cc_on等注释）
            },
            build: {
                src: ['dist/apps-<%= pkg.version %>.js'],
                dest: 'apps.min.js'
            }
        },
        concat: {
            dist: {
                options: {
                    banner: ''
                },
                src: [
                    'libs/holder/holder.min.js',
                    'libs/selectize/selectize.min.js', 
                    'libs/bootstrap/bootstrap.min.js', 
                    'libs/angular/angular.min.js', 
                    'libs/angular/angular-animate.min.js', 
                    'libs/angular/angular-aria.min.js', 
                    'libs/angular/angular-sanitize.js', 
                    'libs/angular/angular-cookies.min.js', 
                    'libs/angular/angular-route.min.js', 
                    'libs/angular-loading-bar/loading-bar.min.js', 
                    'libs/moment/moment-with-locales.min.js', 
                    'libs/angular-moment/angular-moment.min.js', 
                    'libs/highlight/highlight.js', 
                    'libs/marked/marked.min.js', 
                    'libs/marked/angular-marked.min.js', 
                    'libs/codemirror/lib/codemirror.js', 
                    'libs/codemirror/addon/mode/overlay.js', 
                    'libs/codemirror/mode/xml/xml.js', 
                    'libs/codemirror/mode/markdown/markdown.js', 
                    'libs/codemirror/mode/gfm/gfm.js', 
                    'libs/codemirror/mode/javascript/javascript.js', 
                    'libs/codemirror/mode/css/css.js', 
                    'libs/codemirror/mode/htmlmixed/htmlmixed.js', 
                    'libs/codemirror/mode/clike/clike.js', 
                    'libs/codemirror/mode/python/python.js', 
                    'libs/codemirror/mode/meta.js', 
                    'libs/uikit/core.min.js', 
                    'libs/uikit/components/htmleditor.js', 
                    'libs/ng-uikit/ng-uikit.js', 
                    'libs/angular-ui/ui-bootstrap.js', 
                    'libs/ng-holder/holder.js', 
                    'libs/angular-selectize/selectize.js', 
                    'apps/**/*.js'
                ],
                dest: 'dist/apps-<%= pkg.version %>.js'
            },
            dist_tpls: {
                options: {
                    banner: '<%= meta.banner %><%= meta.all %>\n<%= meta.tplmodules %>\n'
                },
                src: [],
                dest: '<%= dist %>/<%= filename %>-tpls-<%= pkg.version %>.js'
            }
        },
        closurecompiler: {
            minify: {
                files: {
                    "apps.min.js": ['dist/apps.min.js']
                },
                options: {
                    "compilation_level": "SIMPLE_OPTIMIZATIONS",

                    // Plus a simultaneous processes limit
                    "max_processes": 5,

                    // And an option to add a banner, license or similar on top
                    "banner": "/* wifi manager js */"
                }
            }
        },
        uncss: {
          dist: {
            files: {
              '../css/site.css': [
                'http://127.0.0.1:8000/',
                'http://127.0.0.1:8000/posts/2',
                'http://127.0.0.1:8000/post/2',
                'http://127.0.0.1:8000/signin'
              ]
            }
          }
        },
        cssmin: {
            options: {
                shorthandCompacting: false,
                roundingPrecision: -1
            },
            target: {
                files: {
                    '../css/site.min.css': [
                        '../css/loading-bar.min.css',
                        '../css/pygments/vs.css',
                        '../css/highlight/vs.css',
                        '../css/codemirror.css',
                        '../css/uikit/htmleditor.min.css',
                        '../css/selectize/selectize.bootstrap3.css',
                        '../css/bootstrap-theme.css',
                        '../css/dropdown.css',
                        '../css/site.css'
                    ]
                }
            }
        },
    });

    // 加载提供"uglify"任务的插件
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-uncss');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // 默认任务
    grunt.registerTask('default', [
        'concat:dist', 
        'uglify',
        'uncss',
        'cssmin'
    ]);
}