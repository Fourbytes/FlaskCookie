// Load the plugins
var gulp = require('gulp');
var sass = require('gulp-sass')
var sassInheritance = require('gulp-sass-inheritance');
var minifyCss = require('gulp-minify-css');
var babel = require('gulp-babel');
var cache = require('gulp-cached')
var duration = require('gulp-duration');
var bower = require('gulp-bower');
var sourcemaps = require('gulp-sourcemaps');
var gulpif = require('gulp-if');
 
gulp.task('bower', function() {
  return bower()
    .pipe(gulp.dest('application/static/vendor/'))
});

gulp.task('global_jsx', function() {
  gulp.src('application/static/jsx/*.jsx')
  .pipe(cache('jsx'))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(sourcemaps.write('./maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('application/static/dist/js/'));
});

gulp.task('global_sass', function() {
  gulp.src('application/static/scss/*.scss')
  .pipe(gulpif(global.isWatching, cache('sass')))
  .pipe(sassInheritance({dir: 'application/static/scss/'}))
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(minifyCss({compatibility: 'ie8'}))
  .pipe(sourcemaps.write('./maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('application/static/dist/css/'));
});

gulp.task('module_jsx', function() {
  gulp.src('application/modules/*/static/jsx/*.jsx', { base: "." })
  .pipe(cache('jsx'))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(sourcemaps.write('../dist/js/maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('../dist/js/'));
});

gulp.task('module_sass', function() {
  gulp.src('application/modules/*/static/scss/*.scss', { base: "." })
  .pipe(gulpif(global.isWatching, cache('sass')))
  .pipe(sassInheritance({dir: 'application/static/scss/'}))
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(minifyCss({compatibility: 'ie8'}))
  .pipe(sourcemaps.write('../dist/css/maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('../dist/css/'));
});

gulp.task('setWatch', function() {
    global.isWatching = true;
});

gulp.task('watch', ['setWatch', 'sass', 'jsx'], function() {
  gulp.watch('{{cookiecutter.app_name}}/static/scss/*.scss', ['sass']);
  gulp.watch('{{cookiecutter.app_name}}/static/jsx/*.jsx', ['jsx']);
});

gulp.task('default', ['sass', 'jsx']);