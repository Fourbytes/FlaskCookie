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
var debug = require('gulp-debug');
var rename = require('gulp-rename');
var path = require('path');


function renameDist(p) {
  p.dirname = path.join(p.dirname, "../dist/");
  if (p.extname == ".css" || p.extname == ".js") {
    p.dirname = path.join(p.dirname, p.extname.substring(1));
  }
}
 
gulp.task('bower', function() {
  return bower()
    .pipe(gulp.dest('application/static/vendor/'))
});

gulp.task('global_jsx', function() {
  gulp.src('application/static/jsx/*.jsx', {base: './'})
  .pipe(cache('jsx'))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(rename(renameDist))
  .pipe(sourcemaps.write('.'))
  .pipe(debug({title: 'global_jsx'}))
  .pipe(gulp.dest('.'));
});

gulp.task('global_scss', function() {
  gulp.src(['application/static/scss/*.scss'], {base: './'})
  .pipe(gulpif(global.isWatching, cache('scss')))
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(minifyCss({compatibility: 'ie8'}))
  .pipe(rename(renameDist))
  .pipe(sourcemaps.write('.'))
  .pipe(gulp.dest('.'))
  .pipe(debug({title: 'global_scss', minimal: false}));
});

gulp.task('module_jsx', function() {
  gulp.src('application/modules/*/static/jsx/*.jsx', {base: './'})
  .pipe(cache('jsx'))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(rename(renameDist))
  .pipe(sourcemaps.write('.'))
  .pipe(debug({title: 'module_jsx'}))
  .pipe(gulp.dest('.'));
});

gulp.task('module_scss', function() {
  gulp.src('application/modules/*/static/scss/*.scss', {base: './'})
  .pipe(gulpif(global.isWatching, cache('scss')))
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(minifyCss({compatibility: 'ie8'}))
  .pipe(rename(renameDist))
  .pipe(sourcemaps.write('.'))
  .pipe(debug({title: 'module_scss'}))
  .pipe(gulp.dest('.'));
});

gulp.task('setWatch', function() {
    global.isWatching = true;
});

gulp.task('watch', ['default', 'setWatch'], function() {
  gulp.watch('application/static/scss/*.scss', ['global_scss']);
  gulp.watch('application/static/jsx/*.jsx', ['global_jsx']);
});

gulp.task('default', ['global_scss', 'global_jsx', 'module_scss', 'module_jsx']);