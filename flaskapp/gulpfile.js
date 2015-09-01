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
 
gulp.task('bower', function() {
  return bower()
    .pipe(gulp.dest('flaskapp/static/vendor/'))
});

// Task configuration
gulp.task('jsx', function() {
  gulp.src('flaskapp/static/jsx/*.jsx')
  .pipe(cache('jsx'))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(sourcemaps.write('./maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('flaskapp/static/dist/js/'));
});

// Task configuration
gulp.task('sass', function() {
  gulp.src('flaskapp/static/scss/*.scss')
  .pipe(cache('sass'))
  .pipe(sassInheritance({dir: 'flaskapp/static/scss/'}))
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(minifyCss({compatibility: 'ie8'}))
  .pipe(sourcemaps.write('./maps'))
  .pipe(duration('Execution Time: '))
  .pipe(gulp.dest('flaskapp/static/dist/css/'));
});

gulp.task('watch', function() {
  gulp.watch('flaskapp/static/scss/*.scss', ['sass']);
  gulp.watch('flaskapp/static/jsx/*.jsx', ['jsx']);
});

gulp.task('default', ['sass', 'jsx']);
gulp.task('test', ['sass', 'jsx']);